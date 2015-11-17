module.exports = {
    context: __dirname + "/src/analytics/analytics/js/core",
    entry: "core.js",
    output: {
        path: __dirname + "/src/analytics/analytics/static/build",
        filename: "bundle.js"
    }
}