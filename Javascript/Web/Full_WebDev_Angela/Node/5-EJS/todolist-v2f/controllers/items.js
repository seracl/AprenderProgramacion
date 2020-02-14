const items = ["Buy Food", "Cook Food", "Eat Food"];
const workItems = [];

// root => GET
exports.getIndex = (req, res, next) => {
    res.render("list", {
        listTitle: 'Today',
        newListItems: items
    });
};//Render a view of all items at root index

exports.getWorkItems = (req, res, next) => {
    res.render("list", {
        listTitle: "Work List",
        newListItems: workItems
    });
};//Render a view of all items at work route

exports.getAbout = (req, res, next) => {
    res.render("about");
};//Render the about view


// root => Post
exports.postItem = (req, res, next) => {
    const item = req.body.newItem;
    const lt = req.body.list;

    if (req.body.list === "Work") {
        workItems.push(item);
        console.log(item);
        res.redirect("/work");
    } else {
        items.push(item);
        console.log(item, lt);
        res.redirect("/");
    }
};//Add item


