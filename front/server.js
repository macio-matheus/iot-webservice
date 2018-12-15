'use strict'

const express = require('express')
const Promise = require('bluebird')
const request = Promise.promisifyAll(require('request'))
const bodyParser = require('body-parser')
const cors = require('cors')

const path  = require('path')
const PORT = 5001
const HOST = '0.0.0.0'

const app = express();
const server = require('http').createServer(app)
const API_BASE_URL = 'http://iot_api:5000'


app.use(bodyParser.json({limit: '50MB', extended: true})) // for parsing application/json
app.use(bodyParser.urlencoded({limit: '50MB', extended: true })) // for parsing application/x-www-form-urlencoded
app.use(cors())
app.use('/views', express.static(__dirname + '/views'))

app.get('/', (req, res) => {
    res.send("<script>window.location.href += 'demo';</script> ")
})


app.get('/demo-iot', (req, res) => {
    //console.log('DOCUMENT ID:',req.params.document_code);
    res.sendFile(path.join(__dirname, "views/index/index.html"));
})


app.post('/api', (req, res) => {

    var json_body = {'text': 'word'};
    request({
        url: API_BASE_URL + '/get_data',
        method: 'POST',
        json: true
    }, function (err, response, body) {
        // console.log(body)
        res.send(body)
    });
})


app.get('*', (req, res)=> {
   res.sendFile(path.join(__dirname, "views/404/index.html"));
});

//show result in console
server.listen(PORT, HOST)
console.log(`Running on http://${HOST}:${PORT}/dashboard/services/`)