

//Layers and Overlays
const Esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 18,
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
});

//Openstreet map tiles
const osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});

//Googlestreet map tiles
const googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 16,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});


function loadExtension(map) {

    //function to load various extension


    //var sidebar = L.control.sidebar('sidebar').addTo(map);
    var ruler = L.control.ruler().addTo(map)

    //Leaflet resetview plugin

    var resetView = L.control.resetView({
        position: "topright",
        title: "Reset view",
        latlng: L.latLng([23.153230032799847, 72.88563487988817]),
        zoom: 18,
    }).addTo(map);



    //Set the location of zoom control to bottom right corner
    L.control.zoom({
        position: 'bottomright'
    }).addTo(map);


    // or, add to an existing map:
    map.addControl(new L.Control.Fullscreen());
    const sidepanelLeft = L.control.sidepanel('mySidepanelLeft', {
        darkMode: 'true',
        tabsPosition: 'left',
        startTab: 'tab-5'
    }).addTo(map);

}


// When the window loads this is called first
$(document).ready(function () {




    // plot the map w
    var map = L.map('map', {
        zoomControl: false,
        loadingControl: true,
    }).setView([28.368498769264686, 77.01619427678051], 14);

    map.flyTo([28.368498769264686, 77.016194276780517], 19, {
    });


    //Default tile 
    // Set to google sattelite imagery
    L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
        attribution: 'Tiles &copy; Google Satellite',
        maxZoom: 22,
        subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
    }).addTo(map);


    var basemaps = {
        "Google Satellite": googleSat,
        'Esri World imagery': Esri_WorldImagery,
        'Open Streetmap': osm
    }


    //Add options to create layers
    layerControl = L.control.layers(basemaps).addTo(map);

    // display scale at the bottom of the page
    L.control.scale().addTo(map);

    //load various extensions
    loadExtension(map)


})
