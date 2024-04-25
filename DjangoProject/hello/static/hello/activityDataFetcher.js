function fetchDataFromSheet(sheetUrl, listId, rowIndex, columnIndexes) {
    const urlWithCacheBusting = `${sheetUrl}?t=${new Date().getTime()}`; // Append timestamp to URL for cache busting
    fetch(urlWithCacheBusting)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            const tableRows = data.match(/<tr[\s\S]*?<\/tr>/g);
            const list = document.getElementById(listId);
            if (rowIndex >= 0 && rowIndex < tableRows.length) {
                const row = tableRows[rowIndex];
                const cellValues = row.match(/<td[\s\S]*?<\/td>/g);
                if (cellValues && cellValues.length > 0) {
                    const rowData = columnIndexes.map(index => {
                        const cell = cellValues[index];
                        let cellContent = cell.match(/<td[^>]*>([\s\S]*?)<\/td>/)[1];
                        cellContent = cellContent.replace(/<br\s*\/?>/gi, '\n');
                        return cellContent;
                    });
                    const listItem = document.createElement('div'); // Changed from 'notlist' for clarity
                    listItem.textContent = rowData.join('\n');
                    list.appendChild(listItem);
                    console.log(list);
                } else {
                    console.error('No cell values found');
                }
            } else {
                console.error('Row index out of bounds');
            }
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}
