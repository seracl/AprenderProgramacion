var myHeaders = new Headers();

var myInit = { method: 'GET',
               headers: myHeaders,
               mode: 'cors',
               cache: 'default' };

var myRequest = new Request('http://api.scb.se/OV0104/v1/doris/en/ssd/', myInit);

fetch(myRequest)
.then(function(response) {
  return response.blob();
})
.then(function(myBlob) {
  var objectURL = URL.createObjectURL(myBlob);
  myImage.src = objectURL;
});

// async function fetchUsers(endpoint) {
//   const res = await fetch(endpoint);
//   let data = await res.json();

//   data = data.map(user => user.username);

//   console.log(data);
// }

// fetchUsers('http://api.scb.se/OV0104/v1/doris/en/ssd/');