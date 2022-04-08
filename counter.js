var apiUrl = 'https://g21z1pb3pa.execute-api.us-east-1.amazonaws.com/prod';
    fetch(apiUrl).then(response => {
      return response.json();
