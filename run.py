from flask import Flask, request
import relays

app = Flask(__name__)

@app.route('/', methods=['POST'])
def result():
    if request.form['relay'] == 'mv_on':
        relays.mv_on()
        return 'master valve on'

    if request.form['relay'] == 'mv_off':
        relays.mv_off()
        return 'master valve off'

    if request.form['relay'] == 'z1_on':
        relays.z1_on()
        return 'zone 1 on'

    if request.form['relay'] == 'z1_off':
        relays.z1_off()
        return 'zone 1 off'

    if request.form['relay'] == 'z2_on':
        relays.z2_on()
        return 'zone 2 on'

    if request.form['relay'] == 'z2_off':
        relays.z2_off()
        return 'zone 2 off'

    if request.form['relay'] == 'z3_on':
        relays.z3_on()
        return 'zone 3 on'

    if request.form['relay'] == 'z3_off':
        relays.z3_on()
        return 'zone 3 off'

    if request.form['relay'] == 'z4_on':
        relays.z4_on()
        return 'zone 4 on'
    
    if request.form['relay'] == 'z4_off':
        relays.z4_off()
        return 'zone 4 off'

    if request.form['relay'] == 'z5_on':
        relays.z5_on()
        return 'zone 5 on'

    if request.form['relay'] == 'z5_off':
        relays.z5_off()
        return 'zone 5 off'

    if request.form['relay'] == 'z6_on':
        relays.z6_on()
        return 'zone 6 on'

    if request.form['relay'] == 'z6_off':
        relays.z6_off()
        return 'zone 6 off'

    if request.form['relay'] == 'z7_on':
        relays.z7_on()
        return 'zone 7 on'

    if request.form['relay'] == 'z7_off':
        relayx.z7_off()
        return 'zone 7 off'
    
    else:
        return 'incorrect key'

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)
