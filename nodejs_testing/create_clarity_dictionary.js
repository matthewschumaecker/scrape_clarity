//this is a node.js version of create_clarity_dictionary that seems to run much faster than the python version
//axios and cheerio required

const axios = require('axios');
const cheerio = require('cheerio');
const fs = require('fs');

async function fetchHtmlContent(url) {
  try {
    const response = await axios.get(url);
    return response.data; // Return the HTML content as a string
  } catch (error) {
    console.error(`Error fetching the URL: ${error}`);
    return null;
  }
}

async function getTableLinks() {
  const htmlContent = await fetchHtmlContent(
    'https://open.epic.com/EHITables/GetTable/_index.htm'
  );
  const $ = cheerio.load(htmlContent);

  const tableLinks = [];
  $('a[href]').each((index, element) => {
    const href = $(element).attr('href');
    if (href.startsWith('./')) {
      tableLinks.push(href.substring(2)); // Remove the './' prefix
    }
  });
  return tableLinks; // Returns a list of table links suffixes
}

async function getTableData(tableName) {
  const link = `https://open.epic.com/EHITables/GetTable/${tableName}`;
  console.log(`Extracting data from ${link}...`);

  const htmlContent = await fetchHtmlContent(link);
  const $ = cheerio.load(htmlContent);

  const tableNameText = $('table.Header2').text();
  const infoResults = $('td.T1Head');
  const infoDescription = $('td[style="white-space: normal;"]');
  const tableDescription = $(infoDescription[0]).text();

  const columns = [];
  for (let i = 1; i < infoResults.length; i += 3) {
    const column = {
      column_name: $(infoResults[i + 1]).text(),
      column_data_type: $(infoResults[i + 2]).text(),
      column_description: $(infoDescription[Math.floor((i + 2) / 3)]).text()
    };
    columns.push(column);
  }

  const tableDict = {
    table_name: tableNameText,
    table_description: tableDescription,
    columns: columns
  };
  return tableDict;
}

async function main() {
  const dataDictionary = [];
  const tableLinks = await getTableLinks();
  for (const link of tableLinks) {
    const tableData = await getTableData(link);
    dataDictionary.push(tableData);
    console.log(`Writing ${link} to dataDictionary...`);
  }

  fs.writeFileSync(
    'clarity_data_dictionary.json',
    JSON.stringify(dataDictionary, null, 4)
  );
  console.log(
    "\n\n\nConverted dictionary to JSON file: 'clarity_data_dictionary.json'"
  );
}


main();