# RSS Feed List

用户在 `MT_DATA/rss/feed_list.yaml` 文件中设置 RSS Feed 列表。

示例如下：

```yaml
feeds:
  - name: Feed 1
    url: http://www.example.com/feed1.xml
    proxy: true
    interval: 2
  - name: Feed 2
    url: http://www.example.com/feed2.xml
  - name: Feed 3
    url: http://www.example.com/feed3.xml
```

对应的 Python 解析方式为：

您可以使用 PyYAML 库来解析 YAML 文件：

```python
import yaml

with open("feeds.yaml", "r") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    feeds = data["feeds"]
    for feed in feeds:
        print("Name:", feed["name"])
        print("URL:", feed["url"])
```
