// Node
// Koordinat di map
nodes = [
    [-6.302286939445012, 107.30263666788876, "[V0] Dinas Sosial Kabupaten Karawang"],
    [-6.274444041783581, 107.27545081274539, "[V1] Kecamatan Karawang Barat"],
    [-6.248831041245198, 107.35653204146328, "[V2] Kecamatan Rawamerta"],
    [-6.15935581925213, 107.29088019953244, "[V3] Kecamatan Rengasdengklok"],
    [-6.174363327404389, 107.33598719471847, "[V4] Kecamatan Kutawaluya"],
    [-6.0765766075880565, 107.17678474393144, "[V5] Kecamatan Batujaya"],
    [-6.046051980055279, 107.1401055970806, "[V6] Kecamatan Pakisjaya"],
    [-6.048595402686564, 107.25020169825245, "[V7] Kecamatan Tirtajaya"],
    [-6.094973198447335, 107.36893046588209, "[V8] Kecamatan Pedes"],
    [-6.1421735155842105, 107.40973662692691, "[V9] Kecamatan Cilebar"],
    [-6.235049237677933, 107.51855001258467, "[V10] Kecamatan Cilamaya Kulon"],
    [-6.250756841591445, 107.58080332809607, "[V11] Kecamatan Cilamaya Wetan"],
    [-6.309397482870587, 107.53494441006194, "[V12] Kecamatan Banyusari"],
    [-6.356352947008921, 107.46870259952021, "[V13] Kecamatan Tirtamulya"],
    [-6.371694299019733, 107.52209174154964, "[V14] Kecamatan Jatisari"],
    [-6.400298850939683, 107.48061482133745, "[V15] Kecamatan Kotabaru"],
    [-6.400914495683963, 107.44300602792109, "[V16] Kecamatan Cikampek"],
    [-6.379591217772605, 107.41757553952661, "[V17] Kecamatan Purwasari"],
    [-6.368513084841798, 107.36979778568171, "[V18] Kecamatan Klari"],
    [-6.38959792989387, 107.36086324124643, "[V19] Kecamatan Ciampel"],
    [-6.51583416423437, 107.22937214150302, "[V20] Kecamatan Tegalwaru"],
    [-6.467829518127596, 107.21561637016019, "[V21] Kecamatan Pangkalan"],
    [-6.338338022071176, 107.25161466997534, "[V22] Kecamatan Telukjambe Barat"],
    [-6.337512560944032, 107.31156939287322, "[V23] Kecamatan Telukjambe Timur"],
    [-6.316661211459145, 107.3220346235559, "[V24] Kecamatan Karawang Timur"],
];

function addAllMarkers() {
    deleteAllMarker();

    var floodIcon = L.icon({
        iconUrl: 'assets/flood.png',
        iconSize: [50, 50]
    });

    var navigatorIcon = L.icon({
        iconUrl: 'assets/navigator.png',
        iconSize: [50, 50]
    });

    $.each(nodes, function(index, value) {
        if (value[2] != "[V0] Dinas Sosial Kabupaten Karawang") {
            L.marker(L.latLng(
                parseFloat(value[0]),
                parseFloat(value[1])), 
                {icon: floodIcon}
            ).addTo(markers).bindPopup(value[2]);
        } else {
            L.marker(L.latLng(
                parseFloat(value[0]),
                parseFloat(value[1])), 
                {icon: navigatorIcon}
            ).addTo(markers).bindPopup(value[2]);
        }
    });

    addAllPath();
}

function addAllPath() {
    // Meminta data list node dari server.py
    $.get("http://192.168.32.228:8005/list", function(data, status) {
        $.each(data, function(i, value) {
            $.each(value, function(j, node) {
                if (node != 0) {
                    L.polygon([nodes[i], nodes[j]]).addTo(markers);
                }
            });
        })
    });
}

function addMarker() {
    deleteAllMarker();
    
    let start = $("#start").val();
    let end = $("#end").val();

    if (start && end) {
        // Meminta data path dari server.py
        checkDistance(start, end);

        $.get(`http://192.168.32.228:8005/path?start=${start}&end=${end}`, function(data) {
            convertLintasanVertex(data.lintasan);
            addPath(data.lintasan);
        });
    }
}

function checkDistance(start, end) {
    $.get(`http://192.168.32.228:8005/distance?start=${start}&end=${end}`, function(data) {
        let distance = data.distance/100;
        $('#distance').val(distance);
    });
}

function addPath(path) {
    var floodIcon = L.icon({
        iconUrl: 'assets/flood.png',
        iconSize: [50, 50]
    });

    var navigatorIcon = L.icon({
        iconUrl: 'assets/navigator.png',
        iconSize: [50, 50]
    });

    $.each(path, function(i, value) {
        if (nodes[value][2] != "[V0] Dinas Sosial Kabupaten Karawang") {
            L.marker(L.latLng(nodes[value]), {icon: floodIcon}).addTo(markers).bindPopup(nodes[value][2]);
        } else {
            L.marker(L.latLng(nodes[value]), {icon: navigatorIcon}).addTo(markers).bindPopup(nodes[value][2]);
        }
        L.polygon([nodes[value], nodes[path[i + 1]]]).addTo(markers);
    });
}

function deleteAllMarker() {
    markers.clearLayers()
}

function convertLintasanVertex(lintasan) {
    const result = lintasan.map(number => `[V${number}]`).join(' - ');
    $('#result-vertex').val(result);
}