module.exports = {
  mode:"jit",
  prefix:"t-",  /* django-bootstrap 과 conflict 방지 => ex. bootstrap -> w-96, tailwind -> t-w-96 */
  content: ["./**/templates/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [],
}
