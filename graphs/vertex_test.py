import my_abstract_pack.abstract_pack as ap

if __name__ == '__main__':
    v0 = ap.Vertex('V0')
    v1 = ap.Vertex('V1')
    v2 = ap.Vertex('V2')
    v0.add_neighbor(v1, 10)
    v2.add_neighbor(v2, 20)
    v0.add_neighbor(v2, 50)
    print ('V0 ID', v0.get_id())
    print ('V0 -> V1 weight', v0.get_weight(v1))
    print('V0 connections', v0.get_connections())
    print ('V0:', v0)

