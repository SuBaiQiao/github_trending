const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "GitHub排行榜";
      return args;
    });
  },
  transpileDependencies: true,
});
