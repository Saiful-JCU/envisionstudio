module.exports = {
    content: ["./templates/**/*.{html,js}", "./static/**/*.{html,js}"],
    theme: {
      extend: {
        colors: {
          primary: "#0E3E4C",
        },
      },
    },
    plugin:{
        tailwindcss: {},
        autoprefixer: {}
    }
}

