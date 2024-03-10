function predictDistrict() {
    let feature1 = document.getElementById('feature1').value;
    let feature2 = document.getElementById('feature2').value;
    let feature3 = document.getElementById('feature3').value;
    let feature4 = document.getElementById('feature4').value;

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            feature1: feature1,
            feature2: feature2,
            feature3: feature3,
            feature4: feature4
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('predicted_district').innerText = 'Predicted District: ' + data.predicted_district;
    })
    .catch(error => console.error('Error:', error));
}