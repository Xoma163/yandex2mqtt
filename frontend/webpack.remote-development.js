/* eslint-disable import/no-extraneous-dependencies */
const {merge} = require("webpack-merge");
const {BundleAnalyzerPlugin} = require("webpack-bundle-analyzer");
const common = require("./webpack.common");

module.exports = merge(common, {
    output: {
        publicPath: `http://${process.env.FRONTEND_IP}:${process.env.FRONTEND_PORT}/static/`,
    },
    devServer: {
        overlay: true,
        hot: false,
        publicPath: `http://${process.env.FRONTEND_IP}:${process.env.FRONTEND_PORT}/static`,
        headers: {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
            "Access-Control-Allow-Headers": "X-Requested-With, content-type, Authorization",
        },
        port: process.env.FRONTEND_PORT,
        stats: "errors-warnings",
    },
    plugins: [
        new BundleAnalyzerPlugin({
            openAnalyzer: false,
        }),
    ],
});