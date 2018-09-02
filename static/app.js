var search = instantsearch({
    // Replace with your own values
    appId: 'E3Z5BWU5LE',
    apiKey: '37f42a7eaff256ed21fe4624bdf01f4f', // search only API key, no ADMIN key
    indexName: 'know-your-school',
    urlSync: true,
    searchParameters: {
      hitsPerPage: 10
    }
  });

search.addWidget(
    instantsearch.widgets.searchBox({
      container: '#search-input'
    })
  );

search.addWidget(
    instantsearch.widgets.hits({
      container: '#hits',
      templates: {
        item: document.getElementById('hit-template').innerHTML,
        empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
      }
    })
  );

  search.addWidget(
    instantsearch.widgets.pagination({
      container: '#pagination'
    })
  );

  search.start();