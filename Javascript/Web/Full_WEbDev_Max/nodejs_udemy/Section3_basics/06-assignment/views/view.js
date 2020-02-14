/* jshint esversion: 6 */
/* jslint node: true */
/* jshint strict: false */

//JS core modules
//Node modules
//Local modules
const dirname = require('../util/path');

var css = `${dirname.public}CSS\\styles.css`;


module.exports.page = {
    header: `
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Node test">
        <meta name="keywords" content="HTML,CSS,XML,JavaScript, NodeJS">
        <meta name="author" content="Raul Clark">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>Route Messages</title>
        
        <link rel="stylesheet" href=${css}>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <head>`,
    navBar: `
    <body>
        <div class="container">
            <nav class="navbar navbar-default">
                <div class="container">
                    <div class="navbar-header">
                        <p class="navbar-brand">DAILY JOURNAL</p>
                    </div>
                    <div>
                        <ul class="nav navbar-nav navbar-right">
                            <li id="home"><a href="/">HOME</a></li>
                            <li id="user"><a href="/user">USER</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        </div>
    `,
        body: ``,
        footer: `
        <div class="footer-padding"></div>
            <div class="footer">
                <p>Made with ❤️ copyright @ 2019. Clark Enterprises</p>
            </div>
        </div>
    </body>`,
        home: `
    <h1>Greethings</h1>
    <div>
        <form action="/create-user" method="POST">
            <input type="text" name="message">
            <button type="submit">Send</button>
        </form>
    </div>`,
        user: `
    <div>
        <h1>Lista</h1>
    </div>
    <ul>
        <li><strong>Elemento</strong></li>
        <li><strong>Elemento</strong></li>
        <li><strong>Elemento</strong></li>
    </ul>`,
        page: function (body) {
            return '<html>'.concat(this.header, this.navBar, body, this.footer, `\n</html>`);
        }
    };