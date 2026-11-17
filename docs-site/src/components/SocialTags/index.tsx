// The link-preview tags of a page with its own social card (front matter field social, plugins/social-cards.mjs):
// the card's size and alt text. The image and description go through PageMetadata.

import React from 'react';

export type Social = { image: string; description?: string; alt: string };

export function socialOf(frontMatter: unknown): Social | undefined {
  return (frontMatter as { social?: Social }).social;
}

export function socialTags(social: Social | undefined, type: string): React.ReactNode[] {
  const tags = [<meta key="type" property="og:type" content={type} />];
  if (social) {
    tags.push(
      <meta key="w" property="og:image:width" content="1200" />,
      <meta key="h" property="og:image:height" content="630" />,
      <meta key="t" property="og:image:type" content="image/png" />,
      <meta key="alt" property="og:image:alt" content={social.alt} />,
      <meta key="talt" name="twitter:image:alt" content={social.alt} />,
    );
  }
  return tags;
}
