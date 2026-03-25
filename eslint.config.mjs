{
  "parser": "@babel/eslint-parser",
  "parserOptions": {
    "ecmaVersion": 2026,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "plugins": ["react"],
  "env": {
    "browser": true,
    "es2026": true
  },
  "rules": {
    "react/react-in-jsx-scope": "off"
  }
}