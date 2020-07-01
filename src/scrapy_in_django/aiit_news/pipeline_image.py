from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy

'''
自定义一个 ImagePipeline
在 settings 中配置 IMAGES_STORE 路径
'''


class SaveImagePipeline(ImagesPipeline):
    # 重写获取资源的请求
    def get_media_requests(self, item, info):
        print(item['img_src'])
        yield scrapy.Request(item['img_src'])

    pass

    # 用于返回保存文件的名称，可以不重写
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    # 资源下载后的操作，比如下载成功后才允许其他Pipeline管道进行处理。可以不重写
    def item_completed(self, results, item, info):
        # results是list列表，里面元素是tuple元组，用于标记下载是否成功
        if not results[0][0]:
            return DropItem('下载失败！')
        print('下载成功！')
        return item
