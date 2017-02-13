"""
Flask server endpoints
"""
import os

from flask import Flask, render_template, request

from data_reader import load_panchayat_agg_stats, load_panchayat_data, \
    agg_by_jobcards, load_jobcard_data
from tables import PanchayatTable, JobcardsTable, HouseHoldTable


app = Flask(__name__)
app.secret_key = \
    b'\xa2?\xb9\xbb\x90^\xf31(D\x08B\xfbB\x8e\x91\xff\xffS\xd9\xc5\xab\xb4f'


@app.route("/")
def panchayats_agg():
    panchayat_data = load_panchayat_agg_stats()
    panchayat_table = PanchayatTable(panchayat_data)
    return render_template('panchayat_view.html', table=panchayat_table)


@app.route("/panchayat/<panchayat_name>")
def panchayat(panchayat_name):
    panchayat_data = load_panchayat_data(panchayat_name)
    jobcards_stats = agg_by_jobcards(panchayat_data)
    jobcards_table = JobcardsTable(jobcards_stats)
    return render_template('jobcards_view.html', table=jobcards_table,
                           panchayat_name=panchayat_name)


@app.route("/jobcard/<jobcard_id>", methods=['GET'])
def jobcard(jobcard_id):
    panchayat_name = request.args.get('panchayat_name')
    panchayat_data = load_panchayat_data(panchayat_name)
    jobcard_id = jobcard_id.split('-')
    end_id = jobcard_id[-2] + '/' + jobcard_id[-1]
    jobcard_id = '-'.join(jobcard_id[:-2] + [end_id])
    jobcard_data = load_jobcard_data(jobcard_id, panchayat_data)
    print(jobcard_data)

    jobcard_table = HouseHoldTable(jobcard_data)

    return render_template('house_hold_view.html', table=jobcard_table,
                           jobcard_id=jobcard_id)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
