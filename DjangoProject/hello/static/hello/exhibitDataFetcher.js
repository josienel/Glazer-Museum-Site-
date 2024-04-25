document.addEventListener('DOMContentLoaded', function() {
    function fetchExhibitData() {
        const exhibitContainer = document.getElementById('exhibit-container');
        const exhibitName = exhibitContainer.getAttribute('data-exhibit-name');

        fetch(`/api/exhibits/${encodeURIComponent(exhibitName)}/`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    const exhibit = data[0];
                    document.getElementById('exhibit-name').textContent = exhibit.ex_name;
                    document.getElementById('exhibit-description').textContent = exhibit.ex_desc;
                } else {
                    console.log('Exhibit not found:', exhibitName);
                }
            })
            .catch(error => {
                console.error('Error fetching exhibit:', error);
            });
    }

    fetchExhibitData();
});
