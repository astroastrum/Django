import React from 'react';
import Layout from '../../components/layout';
import SEO from '../../components/seo';
import WebDesignBlogPage__Header from '../../components/Blog/Subpages/WebDesign/WebDesignBlogPage__Header';
import WebDesignBlogPage__Body from '../../components/Blog/Subpages/WebDesign/WebDesignBlogPage__Body';

const WebDesignCategoryBlogPage = () => (
  <Layout>
    <SEO
      title="Web Design Blog Articles"
      description="Web Design Blog Articles"
      canonicalLink="https://johngrattan.com/blog/web-design/"
    />
    <WebDesignBlogPage__Header
      Tag="header"
      className="bg-img-page-top"
      hOne="Web Design Blog Articles"
    />
    <WebDesignBlogPage__Body
      section="WebDesignBlogPage__Section"
      className="py-md-5 bg-texture-1"
    />
  </Layout>
);

export default WebDesignCategoryBlogPage;