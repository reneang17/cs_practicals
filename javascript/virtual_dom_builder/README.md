# Virtual DOM Builder Exercise

## Objective
A "Virtual DOM" is a simplified, lightweight representation of an actual DOM tree, usually written in basic objects or classes. Frontend libraries (like React or Vue) use this to figure out what changed in the UI before re-drawing the actual browser DOM.

Your goal is to parse an object representation of HTML and traverse it recursively to return an HTML string.

## Instructions
1. Open `index.js` and implement `buildHTML(vnode)`.
2. The function should take a Node object (e.g. `{ tag: 'div', props: { id: 'app' }, children: ['Hello World'] }`) and return the compiled string: `<div id="app">Hello World</div>`.
3. It must cleanly handle string children as Text Nodes, recursively handle child VNodes, and map properties to HTML attributes.
4. Run `node demo.js` to test your function on a sample tree.
5. Reference `solution.js` if you get stuck on the recursion!
