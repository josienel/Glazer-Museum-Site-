// function to get data from published Google sheets
function fetchDataFromSheet(sheetUrl, listId, rowIndex, columnIndexes) {
    fetch(sheetUrl)
        .then(response => response.text())
        .then(data => {
            // get table rows from HTML
            const tableRows = data.match(/<tr[\s\S]*?<\/tr>/g);
            const list = document.getElementById(listId);

            // check rowIndex is within the bounds of tableRows array
            if (rowIndex >= 0 && rowIndex < tableRows.length) {
                const row = tableRows[rowIndex];

                // get table data cells from the row
                const cellValues = row.match(/<td[\s\S]*?<\/td>/g);

                // check that cellValues is not null or empty
                if (cellValues && cellValues.length > 0) {
                    // get text content from specified columns
                    const rowData = columnIndexes.map(index => {
                        const cell = cellValues[index];
                        // get text content from cell
                        let cellContent = cell.match(/<td[^>]*>([\s\S]*?)<\/td>/)[1];
                        // replace HTML entities with actual characters
                        cellContent = cellContent.replace(/&apos;/g, "'");
                        // replace <br> with newline characters
                        cellContent = cellContent.replace(/<br\s*\/?>/gi, '\n');
                        return cellContent;
                    });

                    // make a list item for the row data
                    const listItem = document.createElement('li');
                    listItem.textContent = rowData.join('\n'); // join data with commas if needed
                    list.appendChild(listItem);
                }
            } else {
                console.error('Row index out of bounds.');
            }
        })
        .catch(error => console.error('Error fetching data:', error));
}