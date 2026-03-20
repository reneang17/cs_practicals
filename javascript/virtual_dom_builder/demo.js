const { buildHTML } = require('./index.js');

console.log("--- Starting Virtual DOM Builder Demo ---\n");

const myVirtualDOM = {
  tag: 'div',
  props: { id: 'app', className: 'container' },
  children: [
    {
      tag: 'h1',
      props: { className: 'title' },
      children: ['Welcome to Virtual DOM']
    },
    {
      tag: 'ul',
      props: { className: 'list' },
      children: [
        { tag: 'li', children: ['Item 1'] },
        { tag: 'li', children: ['Item 2'] },
      ]
    }
  ]
};

console.log("Input Virtual DOM Tree Object:");
console.dir(myVirtualDOM, { depth: null });

console.log("\nAttempting to build HTML String...");
const resultString = buildHTML(myVirtualDOM);

console.log("\nOutput HTML:");
console.log(resultString);

console.log("\nExpected Output:");
console.log('<div id="app" class="container"><h1 class="title">Welcome to Virtual DOM</h1><ul class="list"><li>Item 1</li><li>Item 2</li></ul></div>');

if (resultString === '<div id="app" class="container"><h1 class="title">Welcome to Virtual DOM</h1><ul class="list"><li>Item 1</li><li>Item 2</li></ul></div>') {
  console.log("\n✅ Success! Outputs match.");
} else {
  console.log("\n❌ Outputs do not match. Keep trying!");
}
