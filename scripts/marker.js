// Node
// Koordinat di map
nodes = [
    [-6.302286939445012, 107.30263666788876], // Dinas Sosial Kabupaten Karawang
    [-6.274444041783581, 107.27545081274539], // Kecamatan Karawang Barat
    [-6.248831041245198, 107.35653204146328], // Kecamatan Rawamerta
    [-6.15935581925213, 107.29088019953244], // Kecamatan Rengasdengklok
    [-6.174363327404389, 107.33598719471847], // Kecamatan Kutawaluya
    [-6.0765766075880565, 107.17678474393144], // Kecamatan Batujaya
    [-6.046051980015279, 107.1401055970806], // Kecamatan Pakisjaya
    [-6.048595402686564, 107.25020169825245], // Kecamatan Tirtajaya
    [-6.094973198447335, 107.36893046588209], // Kecamatan Pedes
    [-6.1421735155842105, 107.40973662692691], // Kecamatan Cilebar
    [-6.235049237677933, 107.51855001258467], // Kecamatan Cilamaya Kulon
    [-6.250756841591445, 107.58080332809607], // Kecamatan Cilamaya Wetan
    [-6.309397482870587, 107.53494441006194], // Kecamatan Banyusari
    [-6.356352947008921, 107.46870259952021], // Kecamatan Tirtamulya
    [-6.371694299019733, 107.52209174154964], // Kecamatan Jatisari
    [-6.400298850939683, 107.48061482133745], // Kecamatan Kotabaru
    [-6.400914495683963, 107.44300602792109], // Kecamatan Cikampek
    [-6.379591217772605, 107.41757553952661], // Kecamatan Purwasari
    [-6.368513084841798, 107.36979778568171], // Kecamatan Klari
    [-6.38959792989387, 107.36086324124643], // Kecamatan Ciampel
    [-6.51583416423437, 107.22937214150302], // Kecamatan Tegalwaru
    [-6.467829518127596, 107.21561637016019], // Kecamatan Pangkalan
    [-6.338338022071176, 107.25161466997534], // Kecamatan Telukjambe Barat
    [-6.337512560944032, 107.31156939287322], // Kecamatan Telukjambe Timur
    [-6.316661211459145, 107.3220346235559], // Kecamatan Karawang Timur
];

function addAllMarkers() {
    deleteAllMarker();

    $.each(nodes, function(index, value) {
        L.marker(L.latLng(
            parseFloat(value[0]),
            parseFloat(value[1])
          )).addTo(markers);
    });

    addAllPath();
}

function addAllPath() {
    // Meminta data get dari server.py
    $.get("http://192.168.119.236:8000/list", function(data, status) {
        $.each(data, function(i, value) {
            $.each(value, function(j, node) {
                if (node != 0) {
                    L.polygon([nodes[i], nodes[j]]).addTo(markers);
                }
            });
        })
    });
}

function deleteAllMarker() {
    markers.clearLayers()
}

function checkDistance() {
    deleteAllMarker();

    let start = $("#start").val();
    let end = $("#end").val();

    // Meminta data get dari server.py
    $.get(`http://192.168.119.236:8000/path?start=${start}&end=${end}`, function(data) {
        let distance = data.distance/100;
        $('#distance').val(distance);
    });
}

function addMarker() {
    deleteAllMarker();
    
    let start = $("#start").val();
    let end = $("#end").val();

    // Meminta data get dari server.py
    $.get(`http://192.168.119.236:8000/path?start=${start}&end=${end}`, function(data) {
        let distance = data.distance/100;
        $('#distance').val(distance);

        $.each(data.path, function(i, value) {
            L.marker(nodes[value]).addTo(markers);
        });
        
        addPath(data.path);
    });
}

function addPath(path) {
    $.each(path, function(i, value) {
        L.polygon([nodes[value], nodes[path[i + 1]]]).addTo(markers);
    });
}

function calculateDistance(start, finish) {
    let finalPoint = L.latLng(nodes[start], nodes[start]);
    let startPoint = L.latLng(nodes[finish], nodes[finish]);
    dist = finalPoint.distanceTo(startPoint);
    return dist;
}