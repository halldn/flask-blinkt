import blinkt
import math
import time
from flask import Flask, render_template, request
from forms import PulseForm

app = Flask(__name__)
app.secret_key = "development-key"

def fadeChannel(c, t):
    return int(c * (1-math.sin(90 * math.radians(t))))

def pulse_array(r, g, b, s, t):
    blinkt.set_clear_on_exit(True)

    for x in range(s):
        r1 = fadeChannel(r, (x*1.0)/s)
        g1 = fadeChannel(g, (x*1.0)/s)
        b1 = fadeChannel(b, (x*1.0)/s)
        blinkt.set_all(r1, g1, b1)
        blinkt.show()
        time.sleep(t)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/pulse", methods=["GET", "POST"])
def pulse():
  form = PulseForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template('pulse.html', form=form)
    else:
      red_value = form.red_value.data
      green_value = form.green_value.data
      blue_value = form.blue_value.data
      step_count = form.step_count.data
      delay_time = form.delay_time.data

      pulse_array(red_value, green_value, blue_value, step_count, delay_time)

      return render_template('pulse.html', form=form)
  elif request.method == "GET":
    return render_template('pulse.html', form=form)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
