/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// A What's New post's head tags: as Docusaurus' own, with the post's social card and short description
// (plugins/social-cards.mjs) in the description and link-preview tags.

import React from 'react';
import {PageMetadata} from '@docusaurus/theme-common';
import {useBlogPost} from '@docusaurus/plugin-content-blog/client';
import {socialOf, socialTags} from '@site/src/components/SocialTags';

export default function BlogPostPageMetadata(): React.JSX.Element {
  const {assets, metadata} = useBlogPost();
  const {title, description, date, tags, authors, frontMatter} = metadata;
  const social = socialOf(frontMatter);
  return (
    <PageMetadata
      title={frontMatter.title_meta ?? title}
      description={social?.description ?? description}
      keywords={frontMatter.keywords}
      image={social?.image ?? assets.image ?? frontMatter.image}>
      {socialTags(social, 'article')}
      <meta property="article:published_time" content={date} />
      {authors.some((author) => author.url) && (
        <meta
          property="article:author"
          content={authors.map((author) => author.url).filter(Boolean).join(',')}
        />
      )}
      {tags.length > 0 && <meta property="article:tag" content={tags.map((tag) => tag.label).join(',')} />}
    </PageMetadata>
  );
}
