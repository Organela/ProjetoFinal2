const Http = new XMLHttpRequest();
const url = ' http://localhost:64142/';
Http.open("GET", url);
Http.send();

// https://www.freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa/

Http.onreadystatechange = (e) => {
    console.log(Http.responseText)
}