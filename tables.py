from flask_table import Table, Col, LinkCol


class PanchayatTable(Table):
    panchayat_name = Col('Panchayat Name')
    link = LinkCol('Link', 'panchayat',
                   url_kwargs=dict(panchayat_name='panchayat_name'))
    jobcard_count = Col('Jobcard Count')
    jobcard_unique = Col('Jobcard Unique')
    date_max = Col('date max')
    date_min = Col('date min')


class JobcardsTable(Table):
    jobcard_id = Col('Job Card ID')
    link = LinkCol('Link', 'jobcard',
                   url_kwargs=dict(panchayat_name='panchayat_name',
                                   jobcard_id='jobcard_id'))
    count = Col('Count')
    date_max = Col('date max')
    date_min = Col('date min')


class HouseHoldTable(Table):
    name = Col('Name')
    workName = Col('Work Name')
    lastKnownStatus = Col('Last Known Status')
    dateTo = Col('Date To')
