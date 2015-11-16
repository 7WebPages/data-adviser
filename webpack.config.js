module.exports = {
    context: __dirname + "/src/analytics/analytics/static",
    entry: "js/core.js",
    output: {
        path: __dirname + "/dist",
        filename: "bundle.js"
    }
}