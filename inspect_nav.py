with open(r'C:\Engagement-Survey\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

keywords = ['nav-item', 'nav-parent', 'nav-label', 'nav-section', 'data-page', 'nav-sub', 'sidebar-nav']
for i, line in enumerate(lines, 1):
    if any(x in line for x in keywords):
        print(f'{i}: {line}', end='')
