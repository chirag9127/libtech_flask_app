import csv


PANCHAYAT_NAME = 'panchayatName'
JOBCARD = 'jobcard'
DATE_TO = 'dateTo'


def load_records(filename='data/workDetails.csv'):
    records = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)

    return records


def load_records_by_panchayat():
    records = load_records()
    panchayats = {}
    for record in records:
        if record[PANCHAYAT_NAME] not in panchayats:
            panchayats[record[PANCHAYAT_NAME]] = []
        panchayats[record[PANCHAYAT_NAME]].append(record)

    return panchayats


def load_panchayat_agg_stats():
    panchayats = load_records_by_panchayat()

    panchayat_agg_stats = []
    for key, value in panchayats.items():
        panchayat_agg_stats.append({
            'panchayat_name': key,
            'jobcard_count': len(value),
            'jobcard_unique': len(set([rec[JOBCARD] for rec in value])),
            'date_max': max(value, key=lambda x: x[DATE_TO])[DATE_TO],
            'date_min': min(value, key=lambda x: x[DATE_TO])[DATE_TO],
        })
    return panchayat_agg_stats


def load_panchayat_data(panchayat_name):
    panchayats = load_records_by_panchayat()
    return panchayats[panchayat_name]


def load_jobcards_data(data):
    jobcards = {}
    for row in data:
        if row[JOBCARD] not in jobcards:
            jobcards[row[JOBCARD]] = []
        jobcards[row[JOBCARD]].append(row)

    return jobcards


def agg_by_jobcards(data):
    jobcards = load_jobcards_data(data)

    jobcards_stats = []
    for key, value in jobcards.items():
        jobcards_stats.append({
            'jobcard_id': key.replace('/', '-'),
            'panchayat_name': value[0][PANCHAYAT_NAME],
            'count': len(value),
            'date_max': max(value, key=lambda x: x[DATE_TO])[DATE_TO],
            'date_min': min(value, key=lambda x: x[DATE_TO])[DATE_TO],
        })

    return jobcards_stats


def load_jobcard_data(jobcard_id, data):
    jobcards = load_jobcards_data(data)
    return jobcards[jobcard_id]
