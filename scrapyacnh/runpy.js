const CronJob       = require('cron').CronJob;
const {PythonShell} = require('python-shell');


async function startTracking() {
    let options = {
      mode: 'text',
      pythonPath: '/usr/local/bin/python3',
      pythonOptions: ['-u'], // get print results in real-time
      scriptPath: ''
    };

    let job = new CronJob('*/20 * * * * *', function() { //runs every 5 secs in this config
      var d = new Date();
      var now = d.toLocaleDateString('en-UK')+' '+d.toLocaleTimeString('en-UK');

      console.log('Starting at: '+now);
      PythonShell.run('runbot.py', options, function (err, results) {
        if (err) throw err;
        // results is an array consisting of messages collected during execution
        // console.log('results: %j', results);
      });

    }, null, true, null, null, true);
    job.start();
}

startTracking();
