import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title='NexusCommerce AI', layout='wide')

st.title('NexusCommerce AI · 智能跨境运营指挥中心')
st.caption('多Agent协同运营自动化系统（可运行演示版）')

agents = {
    '选品Agent': ['分析TikTok趋势', '识别高利润SKU', '筛选供应链稳定商品'],
    '广告Agent': ['优化Facebook广告', '调整Google投放预算', '生成爆款素材文案'],
    '客服Agent': ['自动回复客户咨询', '处理退款申请', '跟进物流异常订单'],
    '库存Agent': ['预测补货需求', '同步海外仓库存', '预警滞销商品'],
    '财务Agent': ['统计ROI', '计算利润率', '汇总站点销售报表']
}

with st.sidebar:
    st.header('系统控制台')
    market = st.selectbox('目标市场', ['美国', '欧洲', '东南亚', '日本'])
    budget = st.slider('广告预算($)', 1000, 50000, 10000, 1000)
    run = st.button('启动协同任务')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Agent集群状态')
    status = []
    for k in agents:
        status.append([k, random.choice(['在线', '执行中', '待命']), random.randint(80, 99)])
    st.dataframe(pd.DataFrame(status, columns=['Agent', '状态', '健康度%']), use_container_width=True)

with col2:
    st.subheader('今日经营指标')
    metrics = st.columns(3)
    metrics[0].metric('订单数', random.randint(300, 1200), random.randint(10, 80))
    metrics[1].metric('销售额($)', random.randint(10000, 80000), random.randint(500, 3000))
    metrics[2].metric('ROI', round(random.uniform(1.8, 5.2),2), round(random.uniform(0.1,0.8),2))

st.subheader('协同任务日志')
if run:
    logs = []
    for name, tasks in agents.items():
        logs.append([datetime.now().strftime('%H:%M:%S'), name, random.choice(tasks), '完成'])
    st.dataframe(pd.DataFrame(logs, columns=['时间', 'Agent', '任务', '结果']), use_container_width=True)
else:
    st.info('点击左侧【启动协同任务】开始自动化运营。')

st.subheader('系统说明')
st.markdown('''
- 多Agent并行处理选品、广告、客服、库存、财务任务  
- 可扩展接入 Shopify / Amazon / TikTok Shop API  
- 可升级为 AutoGen / CrewAI / LangGraph 架构  
- 当前版本为可运行演示版，适合二次开发
''')
