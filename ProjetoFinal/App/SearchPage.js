var resultado
async function makeRequest() {
    const searchedWord = document.getElementById("search").value

    //const Http = new XMLHttpRequest();
    await console.log("Batati");
    const host = "http://localhost:58424/";
    const response = await axios.get(host + searchedWord);
    resultado = response.data;

}

// https://www.freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa/
