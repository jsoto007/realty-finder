

fetch(`https://phl.carto.com/api/v2/sql?q=SELECT * FROM opa_properties_public`)
    .then((resp) => {
      if (resp.ok) {
        resp.json().then((meetings) => console.log(meetings))
      }
    })