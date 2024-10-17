// Function to create HTML elements for nested data
// Function to fetch anatomy data
function fetchAnatomyData() {
    document.addEventListener('DOMContentLoaded', function() {
        fetch('http://127.0.0.1:5000/anatomy')
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById('anatomy-container');
                container.innerHTML = '<pre>' + JSON.stringify(data, null, 2) + '</pre>';
            })
            .catch(error => {
                console.error('Error fetching anatomy data:', error);
            });
    });
}
fetchAnatomyData();
//AI consulted