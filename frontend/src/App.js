import React, { Component } from 'react';
import './App.css';
import Map from 'react-d3-map';
// require your <Marker> component
import MarkerGroup from 'react-d3-map';

var data = {
    "type": "Feature",
    "properties": {
      "text": "this is a Point!!!"
    },
    "geometry": {
        "type": "Point",
        "coordinates": [122, 23.5]
    }
}

  var width = 700;
  var height = 700;
  // set your zoom scale
  var scale = 1200 * 5;
  // min and max of your zoom scale
  var scaleExtent = [1 << 12, 1 << 13]
  // set your center point
  var center = [122, 23.5];
  // set your popupContent
  var popupContent = function(d) { return d.properties.text; }

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h1 className="App-title">Climate Change is Real</h1>
        </header>
        </div>
  <Map width= {width} height= {height} scale= {scale} scaleExtent= {scaleExtent} center= {center}></Map>
    );
  }
}

export default App;
