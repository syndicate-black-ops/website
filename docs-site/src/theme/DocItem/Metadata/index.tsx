/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// A doc page's head tags: as Docusaurus' own, with the page's social card and short description
// (plugins/social-cards.mjs) in the description and link-preview tags.

import React from 'react';
import {PageMetadata} from '@docusaurus/theme-common';
import {useDoc} from '@docusaurus/plugin-content-docs/client';
import {socialOf, socialTags} from '@site/src/components/SocialTags';

export default function DocItemMetadata(): React.JSX.Element {
  const {metadata, frontMatter, assets} = useDoc();
  // the docs plugin's front matter (metadata), where plugins/social-cards.mjs adds the field social
  const social = socialOf(metadata.frontMatter);
  return (
    <PageMetadata
      title={metadata.title}
      description={social?.description ?? metadata.description}
      keywords={frontMatter.keywords}
      image={social?.image ?? assets.image ?? frontMatter.image}>
      {socialTags(social, 'article')}
    </PageMetadata>
  );
}
