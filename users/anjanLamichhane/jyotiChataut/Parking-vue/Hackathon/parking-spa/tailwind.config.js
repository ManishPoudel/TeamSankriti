/** @type {import('tailwindcss').Config} */
const colors = require ('tailwindcss/colors')
export default {
  content: [
    './public/**/*.html',
    './src/**/*.{js,jsx,ts,tsx,vue}',
  ],
  colors:
  {
    pink: colors.pink
  },
  theme: {
    extend: {},
  },
  plugins: [],
}

