import requests
import json
import time
import csv
from urllib.parse import urljoin
from datetime import datetime

class LinuxDoAPIClient:
    def __init__(self, base_url="https://linux.do"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'ResearchBot/1.0 (+https://example.com/research)',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
        
    def get_site_info(self):
        """获取网站基本信息"""
        try:
            response = self.session.get(
                urljoin(self.base_url, '/site.json'),
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            else:
                print(f"获取site.json失败，状态码: {response.status_code}")
                return None
        except Exception as e:
            print(f"获取网站信息失败: {e}")
            return None
    
    def explore_available_apis(self):
        """探索可用的API端点"""
        print("探索可用的API端点...")
        
        # Discourse常见的API端点
        api_endpoints = [
            '/categories.json',
            '/latest.json',           # 最新帖子
            '/top.json',              # 热门帖子
            '/posts.json',            # 帖子
            '/users.json',            # 用户
            '/tags.json',             # 标签
            '/about.json',            # 关于页面
            '/search.json',           # 搜索
        ]
        
        available_apis = []
        
        for endpoint in api_endpoints:
            try:
                time.sleep(1)  # 请求间隔
                response = self.session.get(
                    urljoin(self.base_url, endpoint),
                    timeout=10
                )
                
                if response.status_code == 200:
                    print(f"✅ {endpoint}: 可用")
                    available_apis.append(endpoint)
                else:
                    print(f"❌ {endpoint}: 不可用 ({response.status_code})")
                    
            except Exception as e:
                print(f"❌ {endpoint}: 错误 - {e}")
        
        return available_apis
    
    def get_categories(self):
        """获取分类信息"""
        try:
            response = self.session.get(
                urljoin(self.base_url, '/categories.json'),
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get('category_list', {}).get('categories', [])
            return []
        except Exception as e:
            print(f"获取分类失败: {e}")
            return []
    
    def get_latest_topics(self, page=0):
        """获取最新话题"""
        try:
            params = {'page': page}
            response = self.session.get(
                urljoin(self.base_url, '/latest.json'),
                params=params,
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get('topic_list', {}).get('topics', [])
            return []
        except Exception as e:
            print(f"获取最新话题失败: {e}")
            return []
    
    def get_top_topics(self, period='daily'):
        """获取热门话题"""
        try:
            params = {'period': period}
            response = self.session.get(
                urljoin(self.base_url, '/top.json'),
                params=params,
                timeout=10
            )
            if response.status_code == 200:
                return response.json().get('topic_list', {}).get('topics', [])
            return []
        except Exception as e:
            print(f"获取热门话题失败: {e}")
            return []
    
    def get_topic_posts(self, topic_id):
        """获取特定话题的帖子"""
        try:
            response = self.session.get(
                urljoin(self.base_url, f'/t/{topic_id}.json'),
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"获取话题 {topic_id} 的帖子失败: {e}")
            return None
    
    def search_topics(self, query, page=0):
        """搜索话题"""
        try:
            params = {
                'q': query,
                'page': page
            }
            response = self.session.get(
                urljoin(self.base_url, '/search.json'),
                params=params,
                timeout=10
            )
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"搜索话题失败: {e}")
            return None

class DataProcessor:
    """数据处理类"""
    
    @staticmethod
    def process_site_info(site_data):
        """处理网站信息"""
        if not site_data:
            return None
            
        processed = {
            'title': site_data.get('title'),
            'description': site_data.get('description'),
            'topics_count': site_data.get('topics_count'),
            'posts_count': site_data.get('posts_count'),
            'users_count': site_data.get('users_count'),
            'categories_count': site_data.get('categories_count'),
            'created_at': site_data.get('created_at'),
            'updated_at': datetime.now().isoformat()
        }
        return processed
    
    @staticmethod
    def process_topics(topics):
        """处理话题列表"""
        processed_topics = []
        for topic in topics:
            processed = {
                'id': topic.get('id'),
                'title': topic.get('title'),
                'slug': topic.get('slug'),
                'posts_count': topic.get('posts_count'),
                'reply_count': topic.get('reply_count'),
                'views': topic.get('views'),
                'like_count': topic.get('like_count'),
                'created_at': topic.get('created_at'),
                'last_posted_at': topic.get('last_posted_at'),
                'visible': topic.get('visible'),
                'closed': topic.get('closed'),
                'archived': topic.get('archived'),
                'category_id': topic.get('category_id')
            }
            processed_topics.append(processed)
        return processed_topics
    
    @staticmethod
    def save_to_json(data, filename):
        """保存数据到JSON文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ 数据已保存到 {filename}")
        except Exception as e:
            print(f"❌ 保存数据失败: {e}")
    
    @staticmethod
    def save_topics_to_csv(topics, filename):
        """保存话题数据到CSV"""
        if not topics:
            print("❌ 没有数据可保存")
            return
            
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['id', 'title', 'posts_count', 'views', 'like_count', 'created_at']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                
                for topic in topics:
                    writer.writerow({
                        'id': topic.get('id'),
                        'title': topic.get('title'),
                        'posts_count': topic.get('posts_count'),
                        'views': topic.get('views'),
                        'like_count': topic.get('like_count'),
                        'created_at': topic.get('created_at')
                    })
            print(f"✅ 话题数据已保存到 {filename}")
        except Exception as e:
            print(f"❌ 保存CSV失败: {e}")

def main():
    """主函数"""
    print("=" * 60)
    print("Linux.do Discourse API 数据收集工具")
    print("=" * 60)
    
    # 初始化客户端
    client = LinuxDoAPIClient()
    processor = DataProcessor()
    
    # 1. 获取网站基本信息
    print("\n1. 获取网站基本信息...")
    site_info = client.get_site_info()
    if site_info:
        processed_site = processor.process_site_info(site_info)
        processor.save_to_json(processed_site, 'linux_do_site_info.json')
        print(f"   - 网站标题: {processed_site.get('title')}")
        print(f"   - 话题数量: {processed_site.get('topics_count')}")
        print(f"   - 帖子数量: {processed_site.get('posts_count')}")
        print(f"   - 用户数量: {processed_site.get('users_count')}")
    else:
        print("❌ 无法获取网站信息")
        return
    
    # 2. 探索可用API
    print("\n2. 探索可用API端点...")
    available_apis = client.explore_available_apis()
    print(f"   发现 {len(available_apis)} 个可用API端点")
    
    # 3. 获取分类信息
    print("\n3. 获取分类信息...")
    categories = client.get_categories()
    if categories:
        processor.save_to_json(categories, 'linux_do_categories.json')
        print(f"   发现 {len(categories)} 个分类")
        for category in categories[:5]:  # 显示前5个分类
            print(f"   - {category.get('name')} (ID: {category.get('id')})")
    
    # 4. 获取最新话题
    print("\n4. 获取最新话题...")
    latest_topics = client.get_latest_topics()
    if latest_topics:
        processed_topics = processor.process_topics(latest_topics)
        processor.save_to_json(processed_topics, 'linux_do_latest_topics.json')
        processor.save_topics_to_csv(processed_topics, 'linux_do_latest_topics.csv')
        print(f"   获取到 {len(latest_topics)} 个最新话题")
        
        # 显示前5个话题
        for topic in processed_topics[:5]:
            print(f"   - {topic.get('title')} (浏览: {topic.get('views')})")
    
    # 5. 获取热门话题
    print("\n5. 获取热门话题...")
    top_topics = client.get_top_topics('daily')
    if top_topics:
        processed_top = processor.process_topics(top_topics)
        processor.save_to_json(processed_top, 'linux_do_top_topics.json')
        print(f"   获取到 {len(top_topics)} 个热门话题")
    
    # 6. 搜索示例
    print("\n6. 搜索Linux相关话题...")
    search_results = client.search_topics('linux')
    if search_results:
        processor.save_to_json(search_results, 'linux_do_search_results.json')
        print(f"   搜索到 {search_results.get('posts', [])} 个相关帖子")
    
    print("\n" + "=" * 60)
    print("数据收集完成!")
    print("=" * 60)
    print("生成的文件:")
    print("✅ linux_do_site_info.json - 网站基本信息")
    print("✅ linux_do_categories.json - 分类信息") 
    print("✅ linux_do_latest_topics.json - 最新话题")
    print("✅ linux_do_latest_topics.csv - 最新话题(CSV格式)")
    print("✅ linux_do_top_topics.json - 热门话题")
    print("✅ linux_do_search_results.json - 搜索结果")
    
    print("\n使用说明:")
    print("📊 所有数据仅可用于构建搜索索引")
    print("🚫 禁止用于AI模型训练")
    print("⚖️ 遵守内容信号: search=yes, ai-train=no")
    print("🤝 尊重API使用限制")

if __name__ == "__main__":
    main()