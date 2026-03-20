function buildHTML(vnode) {
  // Base case: Text node
  if (typeof vnode === 'string' || typeof vnode === 'number') {
    return String(vnode);
  }

  // Opening tag
  let html = `<${vnode.tag}`;

  // Add properties/attributes
  if (vnode.props) {
    for (const [key, value] of Object.entries(vnode.props)) {
      if (key === 'className') {
        html += ` class="${value}"`;
      } else {
        html += ` ${key}="${value}"`;
      }
    }
  }

  html += '>';

  // Recursively process children
  if (vnode.children && Array.isArray(vnode.children)) {
    for (const child of vnode.children) {
      html += buildHTML(child);
    }
  }

  // Closing tag
  html += `</${vnode.tag}>`;

  return html;
}

module.exports = { buildHTML };
