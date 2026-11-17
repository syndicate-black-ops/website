import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Author from '@theme-original/Blog/Components/Author';
import type AuthorType from '@theme/Blog/Components/Author';
import type {WrapperProps} from '@docusaurus/types';

// The post author's picture through useBaseUrl: an address from the site root (authors.yml image_url /img/...)
// becomes ./img/... in the offline manual (hash router, opened from disk), and stays as it is on the website
type Props = WrapperProps<typeof AuthorType>;

export default function AuthorWrapper(props: Props): React.JSX.Element {
  const {imageURL} = props.author;
  const image = useBaseUrl(imageURL ?? '');
  return <Author {...props} author={{...props.author, imageURL: imageURL ? image : imageURL}} />;
}
