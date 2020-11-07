var result
async function makeRequest() {
    const searchedWord = document.getElementById("search").value
    //const Http = new XMLHttpRequest();
    await console.log("Batati");
    const host = "http://localhost:5555/";
    const response = await axios.get(host + searchedWord);
    result = response.data;

    createResultFromRequest();
}

function createResultFromRequest() {
    var json = JSON.stringify(result);
    console.log(result);
    Object.keys(json).forEach(element => {
        tag = document.createElement("P");
        tag.innerHTML = result[element].name + ": " + result[element].count;  
        document.body.appendChild(tag);
    });
    //document.body.appendChild(document.createTextNode(json))// Insert json into to the screen
    
}

// https://www.freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa/
