import os


def generate_hugo_template(word_count, step=500):
    template_start = '''
{{- $index := slice -}}
{{- range $page := $.Site.RegularPages -}}
  {{- $cleaned := slice -}}
  {{- $cleaned = $page.Plain}}
  {{- $cleaned = replace $cleaned "\\\\r" ""}}
  {{- $cleaned = replace $cleaned "\\\\n" ""}}
  {{- $cleaned = replace $cleaned "\\\\u0026rsquo;" "'"}}
  {{- $cleaned = replace $cleaned "\\\\u0026amp;" "&"}}
  {{- $cleaned = replace $cleaned "\\\\u0026#34;" "\\""}}
  {{- $cleaned = replace $cleaned "\\\\u0026#39;" "'"}}
  {{- $cleaned = replace $cleaned "\\\\u0026ndash;" "-"}}
  {{- $cleaned = replace $cleaned "\\\\u0026gt;" ">"}}
  {{- $cleaned = replace $cleaned "\\\\u0026quot;" "\\""}}
  {{- $cleaned = replace $cleaned "\\\\u0026ldquo;" "“"}}
  {{- $cleaned = replace $cleaned "\\\\u0026rdquo;" "”"}}
  {{- $chunked := slice -}}
  {{- $chunked = $chunked | append (substr $cleaned 0 500) -}}'''

    template_middle = '\n'.join(
        f'  {{{{- if gt (countwords $cleaned) {i} }}}}\n    {{{{- $chunked = $chunked | append (substr $cleaned {i} {step}) -}}}}\n  {{{{- end -}}}}'
        for i in range(step, word_count + 1, step)
    )

    template_end = '''
  {{- range $i, $c := $chunked -}}
    {{- $index = $index | append (dict "objectID" (print $page.File.UniqueID "_" $i) "content" $c "order" $i "title" $page.Title "date" $page.Date "url" $page.Permalink "tags" $page.Params.tags "categories" $page.Params.Categories) -}}
  {{- end -}}
{{- end -}}
{{- $index | jsonify -}}'''

    return template_start + template_middle + template_end

# 创建模板
template = generate_hugo_template(15000)

# 获取当前脚本的父目录
script_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 获取模板文件的路径
template_path = os.path.join(script_dir, 'layouts', 'list.algolia.json')

# 保存到文件
with open(template_path, 'w', encoding='utf-8') as f:
    f.write(template)

print("模板被保存到 layouts/list.algolia.json")