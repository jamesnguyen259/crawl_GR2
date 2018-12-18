var express = require('express');
var app = express();
var mapController = require('./controller/map');
var path = require('path');

app.set('view engine', 'pug')
app.set('views', './views')
app.use(express.static(path.join(__dirname, 'public')));
app.get('/', mapController.getMapView)

app.listen(3000, function () {
  console.log('Test map on port 3000!');
})
