/** When your routing table is too long, you can split it into small modules**/

import Layout from '@/layout'

export default{
    path: '/audio',
    component: Layout,
    redirect: '/audio/canvas',
    alwaysShow: true, // will always show the root menu
    name: 'audio',
    meta: {
        title: '音频可视化',
        icon: 'article-ranking'
    },
    children: [
        {
            path: '/audio/canvas',
            component: () => import('@/views/audio-page/index.vue'),
            name: 'canvas',
            meta: { title: 'canvas+audio',icon:'article-create'}
        },
        {
            path: '/audio/wavesurfer',
            component: () => import('@/views/audio-page/wavesurfer.vue'),
            name: 'wavesurfer',
            meta: { title: 'wavesurfer',icon:'article-create'}
        },
    ]
}

