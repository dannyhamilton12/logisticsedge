import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import type { APIContext } from 'astro';

export async function GET(context: APIContext) {
  const articles = await getCollection('articles', ({ data }) => !data.draft);

  const sortedArticles = articles.sort(
    (a, b) => new Date(b.data.pubDate).getTime() - new Date(a.data.pubDate).getTime()
  );

  return rss({
    title: 'LogisticsEdge',
    description: 'UK logistics, customs, and supply chain intelligence for professionals.',
    site: context.site!,
    items: sortedArticles.map((article) => ({
      title: article.data.title,
      pubDate: article.data.pubDate,
      description: article.data.description,
      link: `/articles/${article.id}/`,
      categories: [article.data.category, ...article.data.tags],
    })),
    customData: '<language>en-gb</language>',
  });
}
