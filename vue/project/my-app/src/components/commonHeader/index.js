/* eslint-disable jsx-a11y/anchor-is-valid */
import React from "react"
import { Layout, Avatar, Button, Dropdown } from 'antd';
import { MenuFoldOutlined } from "@ant-design/icons"
import './index.css'
import {  } from 'react-redux' 

const { Header } = Layout;

const CommonHeader = ({ collapsed }) => {
    // 登出
    const logout = () => {

    }
    const items = [
        {
            key: '1',
            label: (
            <a target="_blank" rel="noopener noreferrer">
                个人中心
            </a>
            ),
        },
        {
            key: '2',
            label: (
            <a onClick={() => logout} target="_blank" rel="noopener noreferrer">
            退出
            </a>
            ),
        },    
    ];
    // 点击展开收起按钮
    const setCollapsed = () => {

    }
    return (
        <Header className="header-container">
            <Button
                type="text"
                icon={ <MenuFoldOutlined /> }
                style={{
                    fontSize: '16px',
                    width: 64,
                    height: 32,
                    backgroundColor: '#fff'
                }}
                onClick={() => { setCollapsed() }}
            />
            <Dropdown 
                menu={{ items }}
            >
                <Avatar size={36} src={<img src={require("../../assets/img/user.png")} alt=""/>} />
            </Dropdown>
        </Header>
    )
}

export default CommonHeader