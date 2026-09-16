const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const start = html.lastIndexOf('<script>');
const end = html.lastIndexOf('</script>');
if (start === -1 || end === -1 || end < start) {
  throw new Error('Script block not found');
}
const script = html.slice(start + 8, end);
try {
  new Function(script);
  console.log('JavaScript syntax OK');
} catch (err) {
  console.error('--- STACK ---');
  console.error(err.stack || err.message || String(err));
  const lines = script.split('\n');
  const match = /line (\d+)/.exec(err.stack || err.message || '');
  const lineNumber = match ? Number(match[1]) : null;
  if (lineNumber) {
    const startLine = Math.max(1, lineNumber - 5);
    const endLine = Math.min(lines.length, lineNumber + 5);
    console.error('--- nearby code ---');
    for (let i = startLine; i <= endLine; i++) {
      console.error(String(i).padStart(4, ' ') + ': ' + (lines[i - 1] || ''));
    }
  }
  process.exit(1);
}
