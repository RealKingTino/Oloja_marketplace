/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./views/templates/*.html"],
  theme: {
    extend: {},
  },
  scripts: {
    build: "npx tailwindcss -i ./views/static/input.css -o ./views/static/output.css --watch"
  },
  plugins: [],
}

